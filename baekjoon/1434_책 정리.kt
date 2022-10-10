fun main() {

    // 파싱
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    val a = readLine()!!.split(" ").map { it.toInt() }.toMutableList()
    val b = readLine()!!.split(" ").map { it.toInt() }
    
    // 계산
    var i = 0
    b.forEach {
        when {
            it <= a[i] -> a[i] -= it
            else -> {
                while (it > a[i]) {
                    i++
                }
                a[i] -= it
            }
        }
    }
    
    // 잔여 처리
    var answer = 0
    a.forEach {
        answer += it
    }
    
    // 출력
    println("$answer")
}
