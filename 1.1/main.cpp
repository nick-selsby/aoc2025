
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <ranges>
#include <charconv>

int dial_change_to_offset(std::string_view text) {
	int val;
	std::from_chars(text.data() + 1, text.data() + text.size(), val);
	return text[0] == 'L' ? -val : val;
}

int calc_password(std::string_view text) {
	int val = 50;
	int count = 0;
	for (auto line : std::views::split(text, '\n')) {
		std::string_view sv(line);
		if (sv.empty()) continue;
		val = (val + dial_change_to_offset(sv)) % 100;
		if (val == 0) count++;
	}
	return count;
}

int main() {
	std::ifstream file("input.txt");
	std::stringstream buffer;
	buffer << file.rdbuf();
	std::string content = buffer.str();
	
	int pass = calc_password(content);
	std::cout << "PASSWORD: " << pass << std::endl;

	return 0;
}