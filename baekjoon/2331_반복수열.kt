import kotlin.math.*

fun main() {

    // 파싱
    var (a, p) = readLine()!!.split(" ")
    var pInt = p.toInt()
    
    // 체크
    var count = 0
    val hash = HashMap<String, Int>()
    while (true) {
        var target = hash.get(a)
        target?.let {
            // 출력
            println(target)
            return
        } ?: run {
            hash.put(a, count)
            count++
            a = dFun(a, pInt)
        }
    }
}

fun dFun(a: String, p: Int): String {
    var value = 0
    a.forEach {
        value += (it.digitToInt().toDouble().pow(p)).toInt()
    }
    
    return value.toString()
}
