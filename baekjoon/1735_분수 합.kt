fun main() {

    // 파싱
    val (a1, b1) = readLine()!!.split(" ").map() { it.toInt() }
    var (a2, b2) = readLine()!!.split(" ").map() { it.toInt() }
    
    // 합 
    var n1 = (a1 * b2) + (a2 * b1)
    var n2 = b1 * b2
    
    // 약분
    val gcd = gcd(n1, n2)
    n1 /= gcd
    n2 /= gcd
    
    // 출력
    println("${n1} ${n2}")
}

fun gcd(n: Int, m: Int): Int {
    return if (n < m) {
        if (n == 0) m else gcd(n, m % n)
    } else {
        if (m == 0) n else gcd(m, n % m)
    }
}
