fun main() {
    
    // 파싱
    val num = readLine()!!.toInt()
    
    // 교환 시작
    var ball = 1
    for (i in 1..num) {
        // 파싱
        val (n1, n2) = readLine()!!.split(" ").map() { it.toInt() }
        
        // 공 위치 체크 후 교환
        if (n1 == ball) {
            ball = n2
        }
        else if (n2 == ball) {
            ball = n1
        }
    }
    
    // 결과 출력
    println(ball)
}
