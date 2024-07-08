import time
import os
import sys
import uuid

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from io import BytesIO
import grpc
import streaming.stt_pb2 as stt_pb2
import streaming.stt_pb2_grpc as stt_pb2_grpc


def run():
    from pydub import AudioSegment

    def mic_streaming_asr(api_token, duration):
        if not api_token:
            raise Exception("API token is not provided")
        print("Recording for 120 seconds")
        try:
            import pyaudio

            format = pyaudio.paInt16
            channels = 1
            rate = 16000
            chunk = 1024
            record_seconds = duration
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk,
            )
            yield stt_pb2.StreamingRequest(
                type=stt_pb2.StreamingRequest.AUTH,
                options=stt_pb2.StreamingOptions(
                    session_id=str(uuid.uuid4()),
                    sample_rate=rate,
                    encoding=stt_pb2.StreamingOptions.LINEAR16,
                    model=stt_pb2.StreamingOptions.UZ_GENERAL,
                    auth_token=api_token,
                ),
            )
            for i in range(0, int(rate / chunk * record_seconds)):
                data = stream.read(chunk)
                yield stt_pb2.StreamingRequest(
                    type=stt_pb2.StreamingRequest.STREAMING,
                    chunk=data,
                )
            stream.stop_stream()
            stream.close()
            audio.terminate()
        except Exception as e:
            print(e)
            from traceback import print_exc

            print_exc()

    with grpc.secure_channel(
        os.getenv("MOHIRAI_API_URL", "grpc.mohir.ai"),
        grpc.ssl_channel_credentials(),
    ) as channel:
        stub = stt_pb2_grpc.RecognizerStub(channel)
        word_offsets = {}
        responses = stub.RecognizeStreaming(
            mic_streaming_asr(
                os.getenv(
                    "MOHIRAI_API_TOKEN",
                ),
                120,
            )
        )

        for response in responses:
            if response.status == stt_pb2.StreamingResponse.END_OF_SESSION:
                print("End of session")
                break

            if response.status == stt_pb2.StreamingResponse.ERROR:
                print("Code:", response.error.code)
                print("Error:", response.error.message, response.error.details)
                break

            if response.status == stt_pb2.StreamingResponse.OK:
                response = response.result
                last_offset = response.offsets[-1] if response.offsets else None
                word_offsets = {
                    (offset["id"] if type(offset) == dict else offset.id): offset
                    for offset in [
                        *word_offsets.values(),
                        # *(
                        #     [
                        #         stt_pb2.TranscriptionWords(
                        #             start=last_offset.end,
                        #             end=last_offset.end,
                        #             word=" | ",
                        #             id=uuid.uuid4().hex,
                        #         )
                        #     ]
                        #     if last_offset
                        #     else []
                        # ),
                        *response.offsets,
                    ]
                }
                # clear console
                print("\033[H\033[J", end="")
                print(
                    " ".join(
                        [
                            offset.word
                            for offset in sorted(
                                [
                                    *word_offsets.values(),
                                    *response.temporary_offsets,
                                ],
                                key=lambda x: x.start,
                            )
                        ]
                    )
                    + ("..." if response.ending_silence_duration > 600 else "")
                )


if __name__ == "__main__":
    run()
