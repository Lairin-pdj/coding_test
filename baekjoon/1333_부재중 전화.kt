fun main() {
    
    // 파싱
    val (n, l, d) = readLine()!!.split(" ").map() { it.toInt() }
    
    // 가능 여부 체크 
    var answer = d
    var play = l
    loop@while (answer <= (l + 5) * n - 5) {
        
        // 노래 시간 체크
        while (answer >= play) {
            if (play <= answer && answer < play + 5) {
                
                break@loop
            }
            
            play += (l + 5)
        }
        
        answer += d
    }
    
    // 결과 출력
    println(answer)
}
