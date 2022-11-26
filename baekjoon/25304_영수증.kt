fun main() {
    
    // 파싱
    val money = readLine()!!.toInt()
    val n = readLine()!!.toInt()
    
    // 가격 합산
    var count = 0
    for (i in 0 until n) {
        val (a, b) = readLine()!!.split(" ").map() { it.toInt() }
        count += a * b
    }
    
    // 출력
    when {
        count == money  -> println("Yes")
        else            -> println("No")
    }
    
}
