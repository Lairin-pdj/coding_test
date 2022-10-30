fun main() {

    // 파싱
    val num = readLine()!!.toInt()
    
    for (i in num downTo 4) {
        var check = true
        
        for (j in i.toString()) {
            if (j != '4' && j != '7') {
                check = false
                break
            }
        }
        
        if (check) {
            println(i)
            break
        }
    }
}
