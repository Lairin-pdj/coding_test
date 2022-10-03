import kotlin.math.*

fun main() {

    val count = MutableList(26, { i -> 0 })
    var top = 0

    // 탐색
    while (true) {
        // 라인 별로 
        val line = readLine()
        if (line == null) {
            break
        } else {
            // 글자 체크
            line.forEach {
                when (it) {
                    in 'a'..'z' -> {
                        count[it - 'a']++
                        top = max(top, count[it - 'a'])
                    }
                }
            }
        }
    }
    
    // 결과 출력0
    count.forEachIndexed { index, it ->
        when {
            it == top -> print((index + 'a'.toInt()).toChar())
        }
    }
}
