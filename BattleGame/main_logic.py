import random
from teams import Team, create_character, generate_ai_team
from characters import Warrior, Tanker

class Game:
    def __init__(self):
        self.player_team = None
        self.ai_team = None

    def setup_game(self):
        # 设置玩家队伍
        team_size = int(input("Enter your team size (default is 3, max is 5): ") or 3)
        self.player_team = Team(team_size)
        
        # 循环让用户为每个角色选择类型和命名，创建角色并添加到队伍中
        for i in range(team_size):
            character_type = input(f"Choose the type for character {i+1} ('Warrior' or 'Tanker'): ")
            character_name = input(f"Name your {character_type}: ")
            new_character = create_character(character_type, character_name)
            self.player_team.add_member(new_character)
        
        # 生成AI队伍
    def generate_ai_team(player_team):
            ai_team = Team(player_team.team_size)
            for _ in range(player_team.team_size):
                character_type = random.choice(["Warrior", "Tanker"])
                ai_member_name = f"AI_{character_type}_{random.randint(1, 100)}"
                ai_member = create_character(character_type, ai_member_name)
                ai_team.add_member(ai_member)
            return ai_team #############################################

    def player_turn(self):
        print("\nPlayer's turn...")
        # 显示可能的行动选项
        print(f"可选行动角色: 1.{self.attacker.name} (攻击者)")###################################
        print(f"敌方角色: 1.{self.name} (可攻击的目标)")

        selected_action = False

        while not selected_action:
            # 询问玩家选择哪个角色进行行动
            attacker_name = input("请输入你要行动的角色名称：").capitalize()

            # 如果玩家选择了正确的角色
            if attacker_name == self.name:
                # 现在玩家需要选择一个行动，我们先让他选择攻击
                print(f"你选择了 {self.name}。可执行的行动: 攻击。")
                action = input(f"请输入'攻击'指令来攻击敌人 {self.name}：").lower()

                if action == '攻击':
                    # 这里使用 '攻击' 指令确认玩家的行动
                    # 现在玩家需要指定攻击目标
                    target_name = input("请输入敌方角色的名字来发动攻击：").capitalize()

                    if target_name == self.name:
                        # 执行攻击逻辑
                        damage = self.attack(self)
                        print(f"{self.name} 攻击了 {self.name}，造成了 {damage} 点伤害。")
                        selected_action = True
                    else:
                        print(f"没有找到名为 {target_name} 的角色，请重试。")
                else:
                    print("未知行动，目前只能执行'攻击'。请重新输入。")
            else:
                print(f"没有找到名为 {attacker_name} 的角色，请重试。")

        print("你的回合结束了。\n")

        
    def ai_turn(self):
        print("AI's turn...")
        # 这里应该实现AI行动逻辑
        # 比如根据某种策略选择攻击
        input("AI is thinking... Press Enter to continue...")  # 暂时的AI行动模拟

    def play_game(self):
        self.setup_game()

        # 游戏主循环
        game_over = False
        while not game_over:
            self.player_turn()
            # 检查游戏是否结束，例如检查队伍是否有生存的角色
            # game_over = self.check_game_over()

            self.ai_turn()
            # 再次检查游戏是否结束
            # game_over = self.check_game_over()

            # 如果实现具体的检查游戏结束逻辑，上述的检查可以取消注释

if __name__ == "__main__":
    game = Game()
    game.play_game()