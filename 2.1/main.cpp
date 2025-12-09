#include <string>
#include <fstream>
#include <sstream>
#include <ranges>
#include <vector>
#include <charconv>
#include <iostream>

using ID = uint64_t;

struct IDRange {
	ID first;
	ID last;
};

std::string read_input() {
	std::ifstream file("input.txt");
	std::stringstream buffer;
	buffer << file.rdbuf();
	std::string content = buffer.str();
	return content;
}

std::vector<IDRange> decode_ranges(std::string_view data) {
	auto offsets = data
		| std::views::split(',')
		| std::views::transform([](auto v) { return std::string_view(v); })
		| std::views::filter([](std::string_view sv) { return !sv.empty(); })
		| std::views::transform([](std::string_view sv) -> IDRange {
			size_t idx = sv.find('-');
			IDRange r;
			std::from_chars(sv.data(), sv.data() + idx, r.first);
			std::from_chars(sv.data() + idx + 1, sv.data() + sv.size(), r.last);
			return r;
			})
		| std::ranges::to<std::vector>()
		;

	return offsets;
}

bool is_id_valid(ID id) {
	std::string s = std::to_string(id);
	if ((s.size() & 1) == 1) return true;
	int result = memcmp(s.data(), s.data() + s.size() / 2, s.size() / 2);
	return result != 0;
}

int main() {
	std::string content = read_input();
	auto id_ranges = decode_ranges(content);

	ID total = 0;
	for (auto& id_range : id_ranges) {
		for (ID id = id_range.first; id < id_range.last + 1; id++) {
			bool valid = is_id_valid(id);
			if (!valid) {
				total += id;
				std::cout << id << std::endl;
			}
		}
	}

	std::cout << "SOLUTION  " << total << std::endl;

	return 0;
}