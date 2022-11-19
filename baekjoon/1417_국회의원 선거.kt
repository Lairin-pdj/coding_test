import java.util.*

fun main() {

    // 파싱
    val n = readLine()!!.toInt()
    var my = readLine()!!.toInt()
    
    // 우선순위 큐 생성
    val pq = PriorityQueue<Int>(Collections.reverseOrder()) 
    for (i in 1 until n) {
        pq.add(readLine()!!.toInt())
    }
    // 표 뺏기
    var answer = 0
    while (pq.isNotEmpty()) {
        val temp = pq.poll()
        when {
            temp >= my      -> { pq.add(temp - 1); my++ }
            else            -> break
        }
        answer++
    }
    
    // 출력
    println(answer)
}
