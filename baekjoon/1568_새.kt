fun main() {

    // 파싱
    var birds = readLine()!!.toInt()
    
    var time = 0
    var count = 1
    
    while (birds != 0) {
        // 노래 처리
        if (birds >= count) {
            birds -= count
            count++
        } else {
            count = 1
            birds -= count
            count++
        }
        
        time++
        
        // 탈출
        if (birds == 0) {
            break
        }
    }
    
    // 결과 출력
    println(time)
}
