import discord
import asyncio

class Vote():
  def __init__(
    self, goal: int, objective: str, client, author):
    
    self.goal = goal
    self.objective = objective
    self.client = client
    self.author = author
    self.status = True
    self.voters = []
    self.total = 1

  async def voting(self):
    print('Iniciou')
    def check(msg):
      return msg.content.startswith('!up')
    
    while True:
      print('Aguardando mensagem')
      vote = await client.wait_for_message(timeout=60*5,check=check)
      if not vote:
        self.status = False
        return False
      if vote.author not in self.voters:
        self.total += 1
        if self.total == self.goal:
          msg = f"\
          Votação encerrada !\n{self.objective} - {self.total}/{self.goal}"
          return True
        self.voters.append(vote.author)
        msg = f"""
        {vote.author} Votou !
        Votos: {self.total}/{self.goal}

        digite !up para votar
        """
        await self.client.send_message(vote.channel, msg)
