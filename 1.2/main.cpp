
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

int idiv(int x, int y) {
	if (x < 0) {
		return (x - y + 1) / y;
	}
	else {
		return x / y;
	}
}

int imod(int x, int y) {
	return x - idiv(x, y) * y;
}

int calc_password(std::string_view text) {
	auto offsets = text
		| std::views::split('\n')
		| std::views::transform([](auto v) { return std::string_view(v); })
		| std::views::filter([](std::string_view sv) { return !sv.empty(); })
		| std::views::transform(dial_change_to_offset)
		;

	int dial = 50;
	int count = 0;

	int last_dial = 50;

	for (int offset : offsets) {
		last_dial = dial;
		dial += offset;

		if (offset >= 0) {
			count += idiv(dial, 100);
		}
		else {
			int divs = -idiv(dial - 1, 100);
			count += divs;
			if (count > 0 && last_dial == 0) count--;
		}

		dial = imod(dial, 100);
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