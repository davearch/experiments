/* David Archuleta Jr. 2017
 * @darchuletajr
 * darchuletajr@gmail.com
 *
 * [2016-07-25] Challenge #277 [Easy] Simplifying fractions
 * from https://www.reddit.com/r/dailyprogrammer/
 */
<?php
function gcd($first, $second){
        $remainder = $second%$first;
            if ($remainder == 0):
                return $first;
            else:
                return gcd($remainder,$first);
            endif;
}
function simplify($first, $second){
        $output = array();
        $gcd    = gcd($first, $second);
        $output['first'] = $first /  $gcd;
        $output['second']= $second / $gcd;
        return '('.$output['first'].','.$output['second'].')';
}
print_r(simplify(4,8));
print_r(simplify(1536,78360));
print_r(simplify(51478,5536));
print_r(simplify(46410,119340));
print_r(simplify(7673,4729));
print_r(simplify(4096,1024));