fun main() {

    // 파싱 및 전처리
    val (nowH, nowM, nowS) = readLine()!!.split(":").map { it.toInt() }
    var now = nowH * 3600 + nowM * 60 + nowS
    val (startH, startM, startS) = readLine()!!.split(":").map { it.toInt() }
    var start = startH * 3600 + startM * 60 + startS
    
    // 계산
    if (now > start) start += 3600 * 24
    val diff = start - now
    
    // 출력
    val h = (diff / 3600).toString().padStart(2, '0')
    val m = ((diff / 60) % 60).toString().padStart(2, '0')
    val s = (diff % 60).toString().padStart(2, '0')
    println("$h:$m:$s")
}
