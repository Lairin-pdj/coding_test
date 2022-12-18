fun main() {
    // 파싱
    val n = readLine()!!.toInt()
    
    // dp
    var count = Triple(1, 1, 1)
    for (i in 1 until n) {
        count = Triple(
            (count.first + count.second + count.third) % 9901, 
            (count.first + count.third) % 9901,
            (count.first + count.second) % 9901
        )
    }
    
    // 답 출력
    println((count.first + count.second + count.third) % 9901)
}
