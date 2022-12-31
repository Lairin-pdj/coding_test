fun main() {
    // 파싱
    var line = readLine()!!
    
    // 그리디
    var check = 0
    val max = line.length
    while (check != max) {
        when {
            (line.substring(check, check + 1) == ".") -> {
                check++
            }
            (check + 4 <= max && line.substring(check, check + 4) == "XXXX") -> {
                line = line.substring(0, check) + "AAAA" + line.substring(check + 4)
                check += 4
            }
            (check + 2 <= max && line.substring(check, check + 2) == "XX") -> {
                line = line.substring(0, check) + "BB" + line.substring(check + 2)
                check += 2
            }
            else -> { // 불가능 케이스
                println(-1)
                return
            }
        }
    }
    
    // 답 출력
    println(line)
}
