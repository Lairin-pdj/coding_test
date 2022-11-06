import kotlin.collections.ArrayDeque

fun main() {

    // 파싱
    var (n, k) = readLine()!!.split(" ").map() { it.toInt() }
    val queue = ArrayDeque<Int>()
    
    // queue 초기 상태 생성
    for (i in 1..n) {
        queue.add(i)
    }
    
    // 출력
    print("<")
    
    while (queue.size != 1) {
        for (i in 1 until k) { queue.add(queue.removeFirst()) }
        print("${queue.removeFirst()}, ")
    }
    
    print("${queue.removeFirst()}>")
}
