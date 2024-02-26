## build c++ node example
clang++  rslidar_driver.cc -lm -lrt -ldl -pthread -std=c++14 -lpcap -ldora_node_api_c -L /home/crp/dora_project/dora-rs/dora/target/release --output build/rslidar_driver -I rs_driver/src


