for i in `seq 10`
do
    echo "Starting client #$i"
    python mcp_client_8.py > "$i.txt" &
done
