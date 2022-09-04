fun main() {

    // 파싱
    var (h, m, s) = readLine()!!.split(" ").map() { it.toInt() }
    val time = readLine()!!.toInt()
    
    // 계산
    s += time % 60
    m += (time / 60) % 60
    h += time / 3600
    
    // 넘침 처리
    if (s >= 60) { 
        s -= 60
        m += 1
    }
    if (m >= 60) { 
        m -= 60
        h += 1
    }
    h %= 24
    
    // 결과출력
    println("$h $m $s")
}
