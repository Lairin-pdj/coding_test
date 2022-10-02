fun main() {
    
    // scenario
    var count = 0
    while (true) {
        // 파싱
        var (o, w) = readLine()!!.split(" ").map { it.toInt() }
        val low: Double = o.toDouble() / 2
        val high = o * 2
        count += 1
        
        // 탈출 처리
        if (o == 0) {
            break
        }
    
        // 쿼리 처리
        while (true) {
            val (action, num) = readLine()!!.split(" ")
            when (action) {
                // feed
                "F" -> {
                    if (w > 0) {
                        w += num.toInt()
                    }
                }
                // exercise
                "E" -> {
                    if (w > 0) {
                        w -= num.toInt()
                    }
                }
                // scenario check
                "#" -> {
                    when {
                        w <= 0 -> println("${count} RIP")
                        w > low && w < high -> println("${count} :-)")
                        else -> println("${count} :-(")
                    }
                    break
                }
            }
        }
    }
}
