fun main(args: Array<String>) {
    
    // 파싱
    val nums = readLine()!!.split(" ")
    var maps = mutableListOf<String>()
    for (i in 1..nums[0].toInt()) {
        maps.add(readLine()!!)
    }
    
    // 카운트
    var checkX = mutableSetOf<Int>()
    var checkY = mutableSetOf<Int>()
    for (i in 0..nums[0].toInt() - 1) {
        for (j in 0..nums[1].toInt() - 1) {
            if (maps[i][j] == 'X') {
                checkX.add(i)
                checkY.add(j)
            }
        }
    }
    
    // 결과 출력
    println(listOf<Int>(nums[0].toInt() - checkX.size, nums[1].toInt() - checkY.size).maxOrNull())
}
