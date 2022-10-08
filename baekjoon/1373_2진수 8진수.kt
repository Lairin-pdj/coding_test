fun main() {

    // 파싱 및 전처리
    var num = readLine()!!
    when (num.length % 3) {
        1 -> num = "00" + num
        2 -> num = "0" + num
    }
    
    // 변환 및 결과 출력
    num.chunked(3).forEach {
        print(it.toInt(2))
    }
}
