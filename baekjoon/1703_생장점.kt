fun main() {
    
    while (true) {
    
        // 파싱
        val nums = readLine()!!.split(" ").map() { it.toInt() }
        
        // 탈출 조건 체크
        if (nums[0] == 0) {
          break  
        } 
        
        // 계산 진행
        var answer = 1
        for (i in 1..nums[0]) {
            answer *= nums[i * 2 - 1]
            answer -= nums[i * 2]
        }
        
        // 결과 출력
        println(answer)
    }
}
