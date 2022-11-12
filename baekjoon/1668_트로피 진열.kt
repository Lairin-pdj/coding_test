fun main() {

    // 파싱
    val n = readLine()!!.toInt()
    val nums = mutableListOf<Int>()
    for (i in 1..n) {
        nums.add(readLine()!!.toInt())
    }
    
    // 좌
    var left = 0
    var temp = 0
    for (i in nums) {
        if (temp < i) {
            left++
            temp = i
        }
    }
    
    // 우
    var right = 0
    temp = 0
    for (i in nums.reversed()) {
        if (temp < i) {
            right++
            temp = i
        }
    }
    
    // 출력
    println("${left}")
    println("${right}")
}
