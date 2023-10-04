# grpc python 教學

紀錄 gRPC 也可以稱 Google RPC, 今天來用 python 把玩😀

## 介紹

官網架構圖

簡單說, RPC 就像你 call 本機的 function,

然後這邊就只是你要先去 stub remote,

接著 call function

![alt tag](https://i.imgur.com/BeHImgV.png)

## 好處以及適合使用時機

- 支援  HTTP/2 效能更好

- Protocol Buffers 輕量, 本身就可以當作文件, 不用另外寫文件

- 自帶簡單的驗證

- 跨語法開發

- 適合使用在微服務(microservices)內部溝通

## 環境安裝

```cmd
pip install grpcio grpcio-tools grpc-interceptor
```

## 定義 proto

很重要, 他就是文檔

[protos/user.proto](protos/user.proto)

## 編譯

範例

``` cmd
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/user.proto
```

`--python_out=.` `--pyi_out=.` `--grpc_python_out=.`

這裡的意思都是放在當前目錄底下,

但我們統一把編譯出來的放到 `service_protos` 資料夾底下

```cmd
python -m grpc_tools.protoc -I./protos --python_out=./service_protos --pyi_out=./service_protos --grpc_python_out=./service_protos ./protos/user.proto
```

這邊會有 import 問題, 請將 `user_pb2_grpc.py` 第5行修改,

原本

```python
import user_pb2 as user__pb2
```

改成以下任一種你喜歡的

```python
import service_protos.user_pb2 as user__pb2

# or
# from service_protos import user_pb2 as user__pb2

# or
# from . import user_pb2 as user__pb2
```

如果你不想修改, 建議就是 `server.py` 和 `clint.py` 放在同一層

## grpc server

✍ server 和 client 都需要編譯後的檔案.

先開啟一個 terminal 執行 server

```cmd
python3 server.py
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

在 `server.py` 中, 加入底下

```python
interceptors = [ExceptionToStatusInterceptor()]
server = grpc.server(
        concurrent.futures.ThreadPoolExecutor(max_workers=10),
        interceptors=interceptors
    )
```

如果你加上這個, 當發生錯誤你會更快的找到問題

加入前

![alt tag](https://i.imgur.com/9rgEXjK.png)

加入後

![alt tag](https://i.imgur.com/82XaPdV.png)

## Reference

* [https://grpc.io/docs/what-is-grpc/introduction/](https://grpc.io/docs/what-is-grpc/introduction/)

* [https://grpc.io/docs/languages/python/basics/](https://grpc.io/docs/languages/python/basics/)

* [https://grpc-interceptor.readthedocs.io/en/latest/](https://grpc-interceptor.readthedocs.io/en/latest/)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](http://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license