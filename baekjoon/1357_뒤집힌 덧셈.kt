fun main() {

    // 파싱
    val (x, y) = readLine()!!.split(" ")
    
    // 계산 및 결과출력
    println("${((x.reversed().toInt() + y.reversed().toInt()).toString()).reversed().toInt()}")
}
