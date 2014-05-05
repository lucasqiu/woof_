
while read line
do
    IN=$line
    declare -a a="(${IN/;/ })";
    if [ ${a[0]} -le 43 -a ${a[1]} -le 43 ] ; then
        res=$(./shash -d -q  ../../data/${a[0]}  ../../data/${a[1]})
        
        if [[ ${res} -lt 10 ]]; then
            # echo $res
            str="${a[0]} ${a[1]}"
            echo "$str $res" >> res.txt
        fi
    else
        echo
    fi
done < 'simi.txt'