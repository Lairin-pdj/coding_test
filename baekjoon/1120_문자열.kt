import kotlin.math.*

fun main() {

    // 파싱
    val (a, b) = readLine()!!.split(" ")
    
    // 계산
    var answer = 50
    for (i in 0..(b.length - a.length)) {
        var temp = 0
        a.zip(b.substring(i until (i + a.length))).map { if (it.first != it.second) temp++ }
        answer = min(answer, temp)
    }
    
    // 출력
    println(answer)
}
