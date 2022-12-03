fun main() {

    // 파싱
    val (n, l) = readLine()!!.split(" ").map() { it.toInt() }
    val nums = (readLine()!!.split(" ").map() { it.toInt() }).toMutableList()
    
    // 정렬
    nums.sort()
    
    // 계산
    var count = 0
    var cover: Int? = null
    nums.forEach { target ->
        cover?.let {
            if (it < target) {
                cover = target + l - 1
                count++
            }
        } ?: run {
            cover = target + l - 1
            count++
        }
    }
    
    // 출력
    println(count)
    
}
