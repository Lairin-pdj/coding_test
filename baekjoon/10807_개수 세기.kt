fun main() {
    
    // 파싱
    val n = readLine()!!.toInt()
    val nums = readLine()!!.split(" ").map() { it.toInt() }
    
    // 찾기 및 출력
    val target = readLine()!!.toInt()
    println(nums.count({ it == target}))
    
}
