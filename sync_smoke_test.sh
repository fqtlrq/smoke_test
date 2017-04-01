filepath=$(cd "$(dirname "$0")"; pwd)/
rsync -e 'ssh' -avl --exclude-from 'exclude.txt' $filepath worker@10.12.9.108:~/script/smoke_test/
