减少特征：
1. build->lewis_build.py 运行后会随机生成加载器代码
2. upx 压缩

使用：
1. 将生成的payload.c的payload填入encodeFunction->lewis_shellcode_encode.py 直接运行会生成加密后的shellcode 还有 key


go build -trimpath -ldflags="-w -s -H=windowsgui"

kali 
默认压缩[upx 程序名.exe]
较快压缩[upx -1 程序名.exe]
较好压缩[upx -9 程序名.exe]
最优压缩[upx --best 程序名.exe]
还原压缩[upx -d 程序名.exe]

install:go get -u -v github.com/google/uuid