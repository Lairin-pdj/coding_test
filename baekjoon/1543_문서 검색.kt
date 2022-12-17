fun main() {
    // 파싱
    val main = readLine()!!
    val word = readLine()!!
    
    // 체크
    var count = 0
    var target = 0
    val maxTarget = main.length - word.length
    while (target <= maxTarget) {
        if (main.substring(target, target + word.length) == word) {
            target += word.length
            count++
        } else {
            target++
        }
    }
    
    // 답 출력
    println(count)
}
