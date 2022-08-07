fun main(args: Array<String>) {
    
    // 파싱
    val nums = readLine()!!
    var maps = mutableListOf<MutableList<Int>>()
    for (i in 1..nums.toInt()) {
        maps.add(readLine()!!.split(" ").map{ it.toInt() }.toMutableList())
    }
    
    // 카운트
    var count: Array<Int> = Array(nums.toInt()){ i -> 0 }
    for (i in 0..nums.toInt() - 1) {
        for (j in i + 1..nums.toInt() - 1) {
            for (k in 0..4) {
                if (maps[i][k] == maps[j][k]) {
                    count[i]++
                    count[j]++
                    break
                }
            }
        }
    }
    
    // 결과 출력
    println(count.indexOf(count.maxOrNull()) + 1)
}
