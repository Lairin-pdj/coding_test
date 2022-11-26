fun main() {
    
    // 파싱
    val target = (1..30).toMutableSet()
    
    // 제거 
    for (i in 0 until 28) {
        val n = readLine()!!.toInt()
        target.remove(n)
    }
    
    // 출력  
    target.forEach {
        println(it)
    }
    
}
