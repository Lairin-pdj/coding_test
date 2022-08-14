fun main() {
    
    // 파싱
    val yeondu = readLine()!!
    
    // 원본 계산
    val oriL = Regex("L").findAll(yeondu).count()
    val oriO = Regex("O").findAll(yeondu).count()
    val oriV = Regex("V").findAll(yeondu).count()
    val oriE = Regex("E").findAll(yeondu).count()
    
    // 팀 별 체크
    val num: Int = readLine()!!.toInt()
    var answer = ""
    var score = -1
    for (i in 1..num) {
        val temp = readLine()!!
        val l = Regex("L").findAll(temp).count() + oriL
        val o = Regex("O").findAll(temp).count() + oriO
        val v = Regex("V").findAll(temp).count() + oriV
        val e = Regex("E").findAll(temp).count() + oriE
        
        var tScore = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
        
        if (tScore > score) {
            answer = temp
            score = tScore
        }
        else if (tScore == score) {
            if (answer > temp) {
                answer = temp
                score = tScore
            }
        }
    }
    
    // 결과 출력
    println(answer)
}
