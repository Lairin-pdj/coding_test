fun main() {

    // 파싱
    val count = readLine()!!
    val nums = readLine()!!.split(" ")
    
    // 계산
    var answer = 0
    val set = mutableSetOf<String>()
    nums.forEach {
        if (set.contains(it)) {
            answer++
        } else {
            set.add(it)
        }
    }
    
    // 출력
    println(answer)
}
