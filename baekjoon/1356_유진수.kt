fun main() {
    // 파싱
    val nums = readLine()!!.chunked(1).map() { it.toInt() }
    
    // 누적 곱
    var temp = 1
    var left = mutableListOf<Int>()
    for (num in nums) {
        temp *= num
        left.add(temp)
    }
    
    temp = 1
    var right = mutableListOf<Int>()
    for (num in nums.reversed()) {
        temp *= num
        right.add(temp)
    }
    right.reverse()
    
    // 체크
    var answer = false
    for (i in 1..nums.size - 1) {
        if (left[i - 1] == right[i]) {
            answer = true
            break
        }
    }
    
    // 결과출력
    when (answer) {
        true -> println("YES")
        false -> println("NO")
    }
}
