fun main() {
    // 파싱
    val n = readLine()!!.toInt()
    val list = mutableListOf<Number>()
    for (i in 0 until n) {
        val temp = readLine()!!
        list.add(Number(temp, operateValue(temp)))
    }
    
    // 정렬
    list.sort()
    
    // 답 출력
    list.forEach {
        println(it.str)
    }
}

// value 계산을 해주는 함수
fun operateValue(str: String): Int {
    var value: Int = 0
    
    str.forEach {
        if (it.toInt() >= 49 && it.toInt() <= 57) {
            value += (it.toInt() - 48)
        }
    }
    
    return value
}

// compareTo를 위한 자료 객체
data class Number(
    val str: String,
    val value: Int
): Comparable<Number> {
    override operator fun compareTo(other: Number): Int {
        if (this.str.length > other.str.length) return 1
        if (this.str.length < other.str.length) return -1
        if (this.value > other.value) return 1
        if (this.value < other.value) return -1
        if (this.str > other.str) return 1
        if (this.str < other.str) return -1
        return 0
    }
}
