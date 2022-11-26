fun main() {
    
    // 파싱
    val nums = readLine()!!.split(" ").map() { it.toInt() }
    
    // 계산 및 출력
    for ((now, need) in nums.zip(listOf(1, 1, 2, 2, 2, 8))) {
        print("${need - now} ")
    }
    
}
