# Mohir.AI Streaming STT API example
This example demonstrates how to use Mohir.AI Streaming STT API with python and microphone.

The API is implemented using gRPC streaming service.
You can find service definitions in [stt.proto](streaming%2Fstt.proto)
The example itself is implemented using pyaudio see: [client.py](streaming%2Fclient.py)


### Description: 
1. Currently, we support only little-endian 16000hz 16-bit signed integer PCM audio format. 

## Installation
1. Register at [Mohir.AI](https://mohir.ai)
2. Create new api token
3. Clone [this](https://github.com/Mohir-ai/streaming-stt-example) repository
4. `cd streaming-stt-example`
5. `pip install -r requirements.txt`

## Usage:
1. set `MOHIRAI_API_TOKEN=<your api token>`
2. `python streaming/client.py`



### Development setup (using Mohir.AI development server)
1. `export MOHIRAI_API_URL=grpc.mohir.uzbekvoice.ai`
2. `export MOHIRAI_API_TOKEN=0a98ff19-ea7f-4c5a-9cc8-e16babd87e44:91825486-85e0-45e3-af9b-86c03c2ec951`
3. `python streaming/client.py`

#### Note
The api is currently under development and may not be available at all times. 
 

### Requirements
- Microphone~
- Python 3.9+
- pip


### If you have any questions or want to report a bug, you can create issue in this repository


#### Compatibility
Unfortunately Chrome browser does not yet support gRPC streaming. Browser implementation will requre you to proxy all chunks through your own websocket implementation to convert them to gRPC streaming.
[More information](https://grpc.io/blog/state-of-grpc-web/)


### Q&A
How to transcode audio to pcm in browser?
You can check how its done in [aws-lex](https://github.com/awslabs/aws-lex-browser-audio-capture/blob/master/lib/worker.js)
