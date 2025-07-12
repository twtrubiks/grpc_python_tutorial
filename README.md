# grpc python 教學

* [Youtube Tutorial - gRPC Python 基礎全攻略：掌握 Protobuf定義以及編譯、HTTP/2 高效能 RPC 開發](https://youtu.be/PBPKiPMxaQc)

gRPC 也可以稱 Google RPC, 今天來用 python 把玩 😀

## 介紹

官網架構圖

![alt tag](https://i.imgur.com/BeHImgV.png)

簡單說，RPC (遠端程序呼叫) 就像你呼叫本機的 function 一樣。

實際上，客戶端 (Client) 會透過一個由 `.proto` 文件編譯產生的「客戶端代理」(Client Stub) 來呼叫遠端函式,

這個 Stub 看起來就像一個本地物件，它會幫你處理好參數打包、網路通訊等細節，

讓你感覺就像直接呼叫本地函式 (實際上是呼叫遠端的函式).

## 好處以及適合使用時機

- 基於 HTTP/2 協定，支援多路復用、標頭壓縮、伺服器推送和雙向串流等特性，相比傳統 REST 具有更高的傳輸效率和更低的延遲

- 原生串流支援 (Streaming), 相較 RESTful 如果要實現需要借助不同的機制或協定(WebSockets, Server-Sent Events (SSE) 或長輪詢等額外技術)

- 預設使用 Protocol Buffers (Protobuf) 作為序列化格式。Protobuf 是二進位格式，傳輸效率高且輕量。`.proto` 文件具備**強型別**特性

- 可從單一的 `.proto` 文件為多種主流程式語言（如 Python, Java, Go, C++, Node.js 等）自動生成類型安全的客戶端和伺服器端程式碼，極大地簡化了跨語言服務的開發與整合

- 適合使用在微服務(microservices)內部溝通

🧐 多路復用 (multiplexing)

沒有多路復用 (類似 HTTP/1.1): 就像一條單線道的隧道。一次只能有一輛車（一個請求或回應）通過。如果前面的車開得慢（回應慢），後面的車就必須等待。如果想同時走更多車，就需要挖更多條獨立的隧道（建立多個 TCP 連接），但這樣成本很高（連接建立的開銷）。

有多路復用 (類似 HTTP/2): 就像一條擁有多條車道的高速公路。雖然整條路（TCP 連接）只有一條，但上面可以同時容納來自不同起點、前往不同終點的多輛車（多個請求和回應）並行前進，它們在各自的車道（串流 Stream）上有序行駛，互不阻塞。

## 環境安裝

```cmd
pip install grpcio grpcio-tools
```

## 定義 proto

第一步驟, 先定義 `proto`, 文檔路徑 [protos/user.proto](protos/user.proto)

這裡面定義了 message 以及 service

## 編譯

第二步驟

指令說明 (說明用, 不要使用這個指令, 原因後面說明)

``` cmd
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/user.proto
```

`-I` or `--proto_path` 指定一個目錄，作為 Protocol Buffer 編譯器 (protoc) 搜尋 `.proto` 定義檔路徑.

`--python_out=.` `--pyi_out=.` `--grpc_python_out=.` 這裡的意思都是放在當前目錄底下,

我們統一把編譯出來的放到 `service_protos` 資料夾底下 (方便管理).

指令範例

(推薦使用以下指令進行編譯，利用路徑映射將生成檔案輸出到獨立的 `service_protos` 目錄並解決 `import` 問題)

```cmd
python -m grpc_tools.protoc -Iservice_protos=./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/user.proto
```

說明 `-Iservice_protos=./protos`

`service_protos` 這將成為生成程式碼中 import 路徑的一部分.

可參考 [user_pb2_grpc.py](service_protos/user_pb2_grpc.py) 底下

```python
......
from service_protos import user_pb2 as service__protos_dot_user__pb2
......
```

可參考 [Generating gRPC interfaces with custom package path](https://grpc.io/docs/languages/python/basics/#generating-grpc-interfaces-with-custom-package-path)

## grpc server

第三步驟

✍ server 和 client 都需要編譯後的檔案.

先開啟一個 terminal 執行 server

```cmd
❯ python3 server.py
Server started, listening on 50051
```

## grpc client

✍ server 和 client 都需要編譯後的檔案.

再開啟一個 terminal 執行 client

```cmd
❯ python3 client.py

details {
  id: 2
  value: "twtrubiks"
}
```

## grpc interceptor

幫助你更好的管理 grpc log

```cmd
pip install grpc-interceptor
```

在 [server.py](server.py) 中, 加入底下 code

```python
......
interceptors = [ExceptionToStatusInterceptor()]
server = grpc.server(
        concurrent.futures.ThreadPoolExecutor(max_workers=10),
        interceptors=interceptors
    )
......
```

如果你加上這個, 當發生錯誤你會更快的找到問題

加入前

![alt tag](https://i.imgur.com/9rgEXjK.png)

加入後

![alt tag](https://i.imgur.com/82XaPdV.png)

## 官方範例

如果你還需要範例可參考 [https://github.com/grpc/grpc/tree/v1.72.0/examples/python](https://github.com/grpc/grpc/tree/v1.72.0/examples/python)

## Reference

* [https://grpc.io/docs/what-is-grpc/introduction/](https://grpc.io/docs/what-is-grpc/introduction/)

* [https://grpc.io/docs/languages/python/basics/](https://grpc.io/docs/languages/python/basics/)

* [https://grpc-interceptor.readthedocs.io/en/latest/](https://grpc-interceptor.readthedocs.io/en/latest/)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](https://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license