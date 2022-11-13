fun main() {

    // 파싱
    val n = readLine()!!.toInt()
    val switches = (readLine()!!.split(" ").map() { it.toInt() }).toMutableList()
    
    // 쿼리 처리
    val times = readLine()!!.toInt()
    for (i in 1..times) {
        val (gender, num) = readLine()!!.split(" ").map() { it.toInt() }
        
        when (gender) {
            1 -> {
                for (j in num..n step(num)) {
                    switches[j - 1] = (1 - switches[j - 1])
                }
            }
            2 -> {
                switches[num - 1] = (1 - switches[num - 1])
                var diff = 1
                while (num - diff > 0 && num + diff <= n) {
                    if (switches[num - 1 - diff] == switches[num - 1 + diff]) {
                        switches[num - 1 - diff] = (1 - switches[num - 1 - diff])
                        switches[num - 1 + diff] = (1 - switches[num - 1 + diff])
                        diff++
                    } else {
                        break
                    }
                }
            }
        }
    }
    
    // 출력
    for (i in 0 until n) {
        if (i % 20 == 0 && i != 0) println()
        print("${switches[i]} ")
    }
}
