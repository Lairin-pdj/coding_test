fun main() {

    // 파싱
    val (a, b, c) = readLine()!!.split(":").map() { it.toInt() }
    
    // 계산
    var answer = 0
    if (60 > a && 60 > b && 60 > c) {
        if (0 < a && a <= 12) answer += 2
        if (0 < b && b <= 12) answer += 2
        if (0 < c && c <= 12) answer += 2
    }
    
    // 출력
    println(answer)
}
