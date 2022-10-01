fun main() {

    // 파싱
    val count = readLine()!!.toInt()
    val nums: List<Int> = readLine()!!.split(" ").map() { it.toInt() }
    val cluster = readLine()!!.toInt()
    
    // 계산
    var size: Long = 0
    nums.forEach{
        val temp = it % cluster
        when (temp) {
            0 -> size += it
            else -> size += it - temp + cluster
        }
    }
    
    // 결과출력
    println("$size")
}
