fun main(args: Array<String>) {
    
    // 파싱
    val nums = readLine()!!.split(" ").map { it.toInt() }
    
    // 계산
    var start = 0
    var end = 0
    var check = 0
    var many = 1
    var count = 1
    var total = 0
    while (check <= nums[1]) {
        // 숫자 저장
        when (check) {
            nums[0] - 1 -> start = total
            nums[1] -> end = total
        }
        
        // 숫자 증가
        total += many
        when {
            many == count -> {
                many++
                count = 1
            }
            else -> {
                count++
            }
        }
        
        check++
    }
    
    // 결과 출력
    println(end - start)
}
