fun main(args: Array<String>) {
    
    while (true) {
        val num = readLine()
        
        if (num != "0") {
        
            var answer: Int = 1
            
            for (i in 0..num!!.length - 1) {
                if (num[i] == '1') {
                    answer += 3
                }
                else if (num[i] == '0') {
                    answer += 5
                }
                else {
                    answer += 4
                }
            }
            
            println(answer)
        }
        else {
            break
        }
    }
}
